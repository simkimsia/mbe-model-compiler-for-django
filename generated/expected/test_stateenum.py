"""
doc_string for test_python_class
"""

import pytest

from expected.stateenum import MainState


class TestMainState:
    """
    doc_string
    """

    def teardown_method(self, test_method):
        pass

    def test_states(self):
        """
        test states
        """
        # assert MainState.DRAFT == MainState.DRAFT.value
        assert MainState.DRAFT.order == 1
        print(MainState.DRAFT)
        print(MainState.DRAFT.name)
        print(MainState.DRAFT.order)
        print(MainState.DRAFT.display)
        print(MainState.DRAFT.proxyclass)
        print(MainState.DRAFT.description)
        assert MainState.DRAFT.order == 1
        assert MainState.DRAFT <= MainState.DRAFT
        assert MainState.DRAFT < MainState.PENDING_VENDOR
        with pytest.raises(TypeError):
            (0 < MainState.DRAFT)
        with pytest.raises(ValueError):
            (MainState.CANCELLED < MainState.DRAFT)
        # assert MainState.PENDING_VENDOR == MainState.PENDING_VENDOR.value
        # assert MainState.PENDING_VENDOR == 2
        # assert MainState.DRAFT.display == "Draft"

        # assert MainState.PENDING_VENDOR.display == "Pending Vendor"
