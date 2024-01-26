# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="INTK <collective@plone.org>" \
      org.label-schema.name="markiezenhof-varnish" \
      org.label-schema.description="markiezenhof Varnish image." \
      org.label-schema.vendor="INTK"

COPY etc/varnish.vcl /etc/varnish/default.vcl
