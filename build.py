#!/usr/bin/env python

from bincrafters import build_template_default

if __name__ == "__main__":
    builder = build_template_default.get_builder(pure_c=False, build_policy="missing", options=["qt:shared=True"])
    builder.run()
