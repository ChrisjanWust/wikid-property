from wikid_property import get_property_label, get_property_id


def test_getters():
    assert get_property_label("P26") == "spouse"
    assert get_property_id("spouse") == "P26"

    # check KeyError is generated when gibberish label
    try:
        get_property_label("P812834810234923993")
    except Exception:
        pass
    else:
        assert False, "get_property_label() with gibberish PID should generate an error"
