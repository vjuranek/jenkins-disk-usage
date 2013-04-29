#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tex_top_jobs as top_jobs
import tex_time_structure as time_struct
import tex_overview as overview

overview.generate("../tex/generated/overview.tex")
top_jobs.generate("../tex/generated/top_jobs.tex", 30)
time_struct.generate("../tex/generated/time_struct.tex", [30,90,180,360,720])
