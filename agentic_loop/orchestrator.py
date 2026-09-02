from .state import BugFixState
from reason.generate_fix import detect_exception
from .retrieval_agent import retrieval_agent
from .reason_agent import reason_agent
from .validation_agent import validation_agent
from .critic_agent import critic_agent



def run_agentic_loop(code):

    state = BugFixState(buggy_code=code)

    state.sanitized_code = code

    # Detect exception type from code
    exception_type, exception_message = detect_exception(state.sanitized_code)

    state.exception_type = exception_type or "None"
    state.exception_message = exception_message or ""
    state = retrieval_agent(state)

    while state.attempts < state.max_attempts:

        state.attempts += 1

        state = reason_agent(state)

        state = validation_agent(state)

        # Update exception type based on real runtime error
        if state.validation_errors:
            state.exception_type = state.validation_errors[0]

        state.history.append({
            "attempt": state.attempts,
            "errors": state.validation_errors
        })

        if state.validation_passed:
            break

        state = critic_agent(state)

    return state