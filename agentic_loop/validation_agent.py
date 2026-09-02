from validation.validate_patch import validate_fix


def validation_agent(state):

    # Run validation checks
    result = validate_fix(
        state.generated_fix,
        state.retrieved_chunks[0].get("rerank_score", 0.0) if state.retrieved_chunks else 0.0
    )

    # Store full validation result
    state.validation_result = result

    # Initialize containers
    state.validation_errors = []
    state.validation_warnings = []

    # Critical failures
    if not result.get("syntax_ok", False):
        state.validation_errors.append("syntax_error")

    if not result.get("compile_ok", False):
        state.validation_errors.append("compile_error")

    # Non-critical warnings
    if not result.get("lint_ok", True):
        state.validation_warnings.append("lint_warning")

    # Validation passes only if no critical errors
    state.validation_passed = len(state.validation_errors) == 0

    return state