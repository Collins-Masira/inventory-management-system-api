from unittest.mock import patch, MagicMock
import cli


def test_display_menu_prints_options(capsys):
    cli.display_menu()
    output = capsys.readouterr().out
    assert "INVENTORY MANAGEMENT SYSTEM" in output
    assert "8. Exit" in output


def test_view_inventory_calls_api_and_prints(capsys):
    mock_resp = MagicMock()
    mock_resp.json.return_value = [{"id": 1, "name": "Coca Cola"}]
    with patch("cli.requests.get", return_value=mock_resp) as mock_get:
        cli.view_inventory()
        mock_get.assert_called_once_with(f"{cli.BASE_URL}/inventory")
        assert "Coca Cola" in capsys.readouterr().out
