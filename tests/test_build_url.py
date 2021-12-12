import pytest
from openpython import OpenSeaClient

@pytest.mark.django_db
def test_success_build_url():
    params = {
        "owner": "test_owner",
    }
    openSeaClient = OpenSeaClient.OpenSeaClient()
    did_succeed, url = openSeaClient.build_url(params=params, module="assets")
    assert did_succeed is True
    order_by = "sale_date"
    order_direction = "desc"
    offset = 0
    limit = 10
    assert url == f'https://api.opensea.io/api/v1/assets/?owner=test_owner&order_by={order_by}&order_direction={order_direction}&offset={offset}&limit={limit}'

def test_failed_build_url():
    params = {}
    openSeaClient = OpenSeaClient.OpenSeaClient()
    did_succeed, url = openSeaClient.build_url(params=params, module="assets")
    assert did_succeed is False
    assert url == "Owner Cannot Be None"