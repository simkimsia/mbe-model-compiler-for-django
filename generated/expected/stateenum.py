from collections import namedtuple
from enum import Enum
from functools import total_ordering

## assume use postgres enum types
## so value will store the enum strings directly and they should be the same spelling as the names
## and that a django model will have a field called status or state and another field called status_path or state_path
## this enum class will directly influence both fields


@total_ordering
class MainState(namedtuple("Status", "display path order_in_path proxyclass description"), Enum):
    DRAFT = "Draft", "happy", 1, "DraftOrder", "Anything that is not sent to vendor"
    PENDING_VENDOR = (
        "Pending Vendor",
        "happy",
        2,
        "PendingVendorOrder",
        "Anything that is in vendor inbox",
    )
    REJECTED_BY_VENDOR = "Rejected by Vendor", "reject", 3, "RejectedOrder", "Rejected by vendor"
    PENDING_PR = (
        "Pending PR",
        "happy",
        4,
        "PendingPROrder",
        "Accepted by vendor and now waiting for PR",
    )
    CANCELLED = (
        "Cancelled",
        "cancel",
        None,
        "CancelledOrder",
        "Any Order past the Draft stage can be cancelled",
    )

    def _is_cancelled(self):
        return self == MainState.CANCELLED

    def __lt__(self, other):
        if self._is_cancelled():
            raise ValueError("Cannot compare CANCELLED with other states")
        if other._is_cancelled():
            raise ValueError("Cannot compare CANCELLED with other states")
        if self.__class__ is other.__class__:
            return self.order_in_path < other.order_in_path
        return NotImplemented

