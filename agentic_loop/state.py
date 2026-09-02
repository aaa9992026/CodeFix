from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class BugFixState:

    buggy_code: str

    sanitized_code: str = ""

    retrieved_chunks: List[Dict[str, Any]] = field(default_factory=list)

    retrieval_context: str = ""

    generated_fix: str = ""

    generated_patch: str = ""

    explanation: str = ""

    validation_passed: bool = False

    validation_errors: List[str] = field(default_factory=list)

    critic_feedback: str = ""

    attempts: int = 0

    max_attempts: int = 3
    
    exception_type: str = ""

    history: List[Dict[str, Any]] = field(default_factory=list)