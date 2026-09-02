import ast

from retrieve.retrieve_similar_code import retrieve_candidates, rerank


def extract_code_keywords(code):

    keywords = set()

    try:
        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.Name):
                keywords.add(node.id)

            elif isinstance(node, ast.Attribute):
                keywords.add(node.attr)

            elif isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):
                    keywords.add(node.func.id)

                elif isinstance(node.func, ast.Attribute):
                    keywords.add(node.func.attr)

    except Exception:
        pass

    return " ".join(sorted(keywords))


def retrieval_agent(state):

    code_keywords = extract_code_keywords(state.sanitized_code)

    exception_type = getattr(state, "exception_type", None) or ""
    exception_message = getattr(state, "exception_message", None) or ""

    query = f"""
Python bug fixing task

Exception type:
{exception_type}

Exception message:
{exception_message}

Code tokens:
{code_keywords}

Buggy code:
{state.sanitized_code}
""".strip()

    print("\nRetrieval query:")
    print(query)
    print()

    retrieved = retrieve_candidates(query)

    reranked = rerank(query, retrieved)

    state.retrieved_chunks = reranked[:5]

    context_chunks = []
    for c in state.retrieved_chunks:
        code = c.get("code")
        if code:
            context_chunks.append(code.strip())

    state.retrieval_context = "\n\n".join(context_chunks)

    return state