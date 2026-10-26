"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Inspect successful and unsuccessful offline response fixtures."""
    # A successful 2xx response should be parsed as a JSON object.
    result = parse_json_response(200, fixture)
    assert result["lesson"] == 13
    print(result)

    # An unsuccessful HTTP status should raise ValueError.
    try:
        parse_json_response(500, fixture)
    except ValueError as error:
        print(f"Caught expected error: {error}")
    else:
        raise AssertionError("Expected ValueError for HTTP status 500")


if __name__ == "__main__":
    main()
