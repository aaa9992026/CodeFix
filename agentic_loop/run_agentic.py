from agentic_loop.orchestrator import run_agentic_loop


def main():

    print("Paste buggy code. Type END when finished:")

    lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        lines.append(line)

    code = "\n".join(lines)

    state = run_agentic_loop(code)

    print("\nExplanation:\n")
    print(state.explanation)

    print("\nPatch:\n")
    print(state.generated_patch)

    print("\nAttempts:", state.attempts)

    print("\nValidation:\n")
    print(state.validation_errors)


if __name__ == "__main__":
    main()