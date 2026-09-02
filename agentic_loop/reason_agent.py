from reason.generate_fix import generate_answer


def reason_agent(state):

    result = generate_answer(state.sanitized_code)

    state.generated_fix = result.get("corrected_function", "")
    state.generated_patch = result.get("diff", "")
    state.explanation = result.get("explanation", "")

    return state