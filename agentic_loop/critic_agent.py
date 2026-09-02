def critic_agent(state):

    if state.validation_passed:
        return state

    errors = "\n".join(state.validation_errors)

    feedback = f"""
Previous fix failed validation.

Errors:
{errors}

Fix the issue with a minimal patch.
"""

    state.critic_feedback = feedback

    return state