from robocorp.log import verify_log_messages_from_log_html


def test_log_with_yield_iterator(tmpdir, ui_regenerate):
    from imp import reload

    from robocorp_log_tests._resources import check_iterators
    from robocorp_log_tests.fixtures import ConfigForTest, basic_log_setup

    from robocorp.log._decoder import (
        MESSAGE_TYPE_YIELD_RESUME,
        MESSAGE_TYPE_YIELD_SUSPEND,
    )

    config = ConfigForTest()
    with basic_log_setup(tmpdir, config=config) as setup_info:
        check_iterators = reload(check_iterators)
        check_iterators.main()

    log_target = setup_info.log_target
    assert log_target.exists()
    msgs = verify_log_messages_from_log_html(
        log_target,
        [
            {
                "message_type": MESSAGE_TYPE_YIELD_RESUME,
                "name": "iterate_entries_in_project",
                "libname": "robocorp_log_tests._resources.check_iterators",
            },
            {
                "message_type": MESSAGE_TYPE_YIELD_SUSPEND,
                "type": "int",
                "value": "2",
            },
            {
                "message_type": "SE",
                "name": "iterator_in_library",
                "libname": "robocorp_log_tests._resources.check_iterators_lib",
                "type": "UNTRACKED_GENERATOR",
            },
        ],
    )
    # for m in msgs:
    #     print(m)
    # setup_info.open_log_target()


def test_log_with_yield_iterator_augassign(tmpdir, ui_regenerate):
    from imp import reload

    from robocorp_log_tests._resources import check_iterators
    from robocorp_log_tests.fixtures import ConfigForTest, basic_log_setup

    from robocorp.log._decoder import (
        MESSAGE_TYPE_YIELD_RESUME,
        MESSAGE_TYPE_YIELD_SUSPEND,
    )

    config = ConfigForTest()
    with basic_log_setup(tmpdir, config=config) as setup_info:
        check_iterators = reload(check_iterators)
        check_iterators.main_yield_augassign()

    log_target = setup_info.log_target
    assert log_target.exists()
    msgs = verify_log_messages_from_log_html(
        log_target,
        [
            {
                "message_type": MESSAGE_TYPE_YIELD_SUSPEND,
                "name": "yield_augassign",
                "libname": "robocorp_log_tests._resources.check_iterators",
                "type": "str",
                "value": "'aug1'",
            },
            {
                "message_type": MESSAGE_TYPE_YIELD_RESUME,
                "name": "yield_augassign",
                "libname": "robocorp_log_tests._resources.check_iterators",
            },
            {
                "message_type": MESSAGE_TYPE_YIELD_SUSPEND,
                "name": "yield_augassign",
                "libname": "robocorp_log_tests._resources.check_iterators",
                "type": "str",
                "value": "' aug2'",
            },
            {
                "message_type": MESSAGE_TYPE_YIELD_RESUME,
                "name": "yield_augassign",
                "libname": "robocorp_log_tests._resources.check_iterators",
            },
            {
                "message_type": MESSAGE_TYPE_YIELD_SUSPEND,
                "name": "yield_augassign",
                "libname": "robocorp_log_tests._resources.check_iterators",
                "type": "str",
                "value": "' aug3'",
            },
            {
                "message_type": MESSAGE_TYPE_YIELD_RESUME,
                "name": "yield_augassign",
                "libname": "robocorp_log_tests._resources.check_iterators",
            },
            {
                "message_type": "EE",
                "type": "GENERATOR",
                "status": "PASS",
            },
        ],
    )
    # for m in msgs:
    #     print(m)
    # setup_info.open_log_target()


def test_log_with_yield_from_iterator(tmpdir, ui_regenerate):
    from imp import reload

    from robocorp_log_tests._resources import check_iterators
    from robocorp_log_tests.fixtures import ConfigForTest, basic_log_setup

    from robocorp.log._decoder import (
        MESSAGE_TYPE_YIELD_FROM_RESUME,
        MESSAGE_TYPE_YIELD_FROM_SUSPEND,
    )

    config = ConfigForTest()
    with basic_log_setup(tmpdir, config=config) as setup_info:
        check_iterators = reload(check_iterators)
        check_iterators.main_yield_from()

    log_target = setup_info.log_target
    assert log_target.exists()
    msgs = verify_log_messages_from_log_html(
        log_target,
        [
            {
                "message_type": MESSAGE_TYPE_YIELD_FROM_SUSPEND,
                "name": "yield_from",
                "libname": "robocorp_log_tests._resources.check_iterators",
            },
            {
                "message_type": MESSAGE_TYPE_YIELD_FROM_RESUME,
                "name": "yield_from",
                "libname": "robocorp_log_tests._resources.check_iterators",
            },
        ],
    )
    # for m in msgs:
    #     print(m)
    # setup_info.open_log_target()


def test_log_with_for_loop(tmpdir, ui_regenerate):
    from imp import reload

    from robocorp_log_tests._resources import check_iterators
    from robocorp_log_tests.fixtures import ConfigForTest, basic_log_setup

    config = ConfigForTest()
    with basic_log_setup(tmpdir, config=config) as setup_info:
        check_iterators = reload(check_iterators)
        check_iterators.for_iter()

    log_target = setup_info.log_target
    assert log_target.exists()
    msgs = verify_log_messages_from_log_html(
        log_target,
        [
            {"message_type": "SE", "name": "for i in range(5)", "type": "FOR"},
            {"message_type": "EE", "type": "FOR", "status": "PASS"},
            {"message_type": "SE", "name": "for i in range(5)", "type": "FOR_STEP"},
            {"message_type": "EA", "name": "i", "type": "int", "value": "2"},
            {
                "message_type": "AS",
                "name": "for_iter",
                "target": "a",
                "type": "int",
                "value": "2",
            },
            {"message_type": "EE", "type": "FOR_STEP", "status": "PASS"},
        ],
    )
    # for m in msgs:
    #     print(m)
    # setup_info.open_log_target()


def test_log_with_for_loop_and_exception(tmpdir, ui_regenerate, str_regression):
    from imp import reload

    from robocorp_log_tests._resources import check_iterators
    from robocorp_log_tests.fixtures import (
        ConfigForTest,
        basic_log_setup,
        pretty_format_logs_from_log_html,
    )

    config = ConfigForTest()
    with basic_log_setup(tmpdir, config=config) as setup_info:
        check_iterators = reload(check_iterators)
        try:
            check_iterators.for_iter_exc()
        except RuntimeError:
            pass

    log_target = setup_info.log_target
    assert log_target.exists()
    str_regression.check(pretty_format_logs_from_log_html(log_target))
    # for m in msgs:
    #     print(m)
    # setup_info.open_log_target()


def test_log_with_for_loop_multiple_targets(tmpdir, ui_regenerate, str_regression):
    from imp import reload

    from robocorp_log_tests._resources import check_iterators
    from robocorp_log_tests.fixtures import (
        ConfigForTest,
        basic_log_setup,
        pretty_format_logs_from_log_html,
    )

    config = ConfigForTest()
    with basic_log_setup(tmpdir, config=config) as setup_info:
        check_iterators = reload(check_iterators)
        check_iterators.for_iter_multiple_targets()

    log_target = setup_info.log_target
    assert log_target.exists()
    str_regression.check(pretty_format_logs_from_log_html(log_target))
    # for m in msgs:
    #     print(m)
    # setup_info.open_log_target()


def test_log_with_for_loop_and_exception_inside_for(
    tmpdir, ui_regenerate, str_regression
):
    from imp import reload

    from robocorp_log_tests._resources import check_iterators
    from robocorp_log_tests.fixtures import (
        ConfigForTest,
        basic_log_setup,
        pretty_format_logs_from_log_html,
    )

    config = ConfigForTest()
    with basic_log_setup(tmpdir, config=config) as setup_info:
        check_iterators = reload(check_iterators)
        check_iterators.for_with_exception()

    log_target = setup_info.log_target
    assert log_target.exists()
    str_regression.check(pretty_format_logs_from_log_html(log_target))
    # for m in msgs:
    #     print(m)
    # setup_info.open_log_target()
