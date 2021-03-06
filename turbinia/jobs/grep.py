# -*- coding: utf-8 -*-
# Copyright 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Job to execute grep task."""

from __future__ import unicode_literals

from turbinia.evidence import TextFile
from turbinia.evidence import FilteredTextFile
from turbinia.evidence import PlasoCsvFile
from turbinia.jobs import TurbiniaJob
from turbinia.workers.grep import GrepTask


class GrepJob(TurbiniaJob):
  """Filter input based on regular expression patterns."""

  # The types of evidence that this Job will process
  evidence_input = [type(TextFile()), type(PlasoCsvFile())]
  evidence_output = [type(FilteredTextFile())]

  def __init__(self):
    super(GrepJob, self).__init__(name='GrepJob')

  def create_tasks(self, evidence):
    """Create task.

    Args:
      evidence: List of evidence object to process

    Returns:
        A list of tasks to schedule.
    """
    tasks = [GrepTask() for _ in evidence]
    return tasks
