"""Stream type classes for tap-webflow."""

from __future__ import annotations

import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_webflow.client import WebflowStream


class FormSubmissionsStream(WebflowStream):
    """Define custom stream."""
    name = "form_submissions"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    records_jsonpath = "$.formSubmissions[*]"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("formId", th.StringType),
        th.Property("displayName", th.StringType),
        th.Property("siteId", th.StringType),
        th.Property("workspaceId", th.StringType),
        th.Property("formResponse", th.ObjectType(
            th.Property("First Name Book Demo", th.StringType),
            th.Property("Last Name Book Demo", th.StringType),
            th.Property("Email Book Demo", th.StringType),
            th.Property("fs_source", th.StringType),
            th.Property("fs_source_cam", th.StringType),
            th.Property("lang", th.StringType),
            th.Property("Company Size", th.StringType),
            th.Property("industry", th.StringType),
            th.Property("Demo Use Type", th.StringType),
            th.Property("devices", th.StringType),
            th.Property("use_type", th.StringType),
        )),
        th.Property("dateSubmitted", th.StringType),
        th.Property("pageId", th.StringType),
        th.Property("publishedPath", th.StringType),
        th.Property("schema", th.ArrayType(th.AnyType)),
        th.Property("site_id", th.StringType),
    ).to_dict()

    @property
    def path(self) -> str:
        """Return the API path."""
        return f"/sites/{self.config.get('site_id')}/form_submissions"

    def get_url_params(
        self,
        context: th.Optional[th.Context],  # noqa: ARG002
        next_page_token: th.Optional[th.Any], # noqa: ARG002
    ) -> dict[str, th.Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        params["limit"] = self.config.get("limit", 1000)
        params["offset"] = 0
        params["elementId"] = self.config.get("form_id")
        return params
