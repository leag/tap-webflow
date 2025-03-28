"""Webflow tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_webflow import streams


class TapWebflow(Tap):
    """Webflow tap class."""

    name = "tap-webflow"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            title="Auth Token",
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "site_id",
            th.StringType,
            required=True,
            title="Form ID",
            description="The ID of the site to sync",
        ),
        th.Property(
            "form_id",
            th.StringType,
            required=True,
            title="Form ID",
            description="The ID of the form to sync",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType,
            title="API URL",
            default="https://api.mysample.com",
            description="The url for the API service",
        ),
        th.Property(
            "user_agent",
            th.StringType,
            description=(
                "A custom User-Agent header to send with each request. Default is "
                "'<tap_name>/<tap_version>'"
            ),
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.WebflowStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.FormSubmissionsStream(self),
        ]


if __name__ == "__main__":
    TapWebflow.cli()
