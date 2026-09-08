class ProjectError(Exception):
    """Base class for project application errors."""


class ValidationError(ProjectError):
    """Raised for invalid input or invalid business state."""


class DuplicateError(ProjectError):
    """Raised for duplicate identifiers."""


class NotFoundError(ProjectError):
    """Raised when an entity is missing."""


class StateTransitionError(ProjectError):
    """Raised for an invalid task status transition."""
