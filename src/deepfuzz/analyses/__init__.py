# Copyright 2025 Fuzz Introspector Authors
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
"""Initialisation of AnalysisInterface instances"""

from deepfuzz import analysis
from deepfuzz.analyses import bug_digestor
from deepfuzz.analyses import driver_synthesizer
from deepfuzz.analyses import engine_input
from deepfuzz.analyses import filepath_analyser
from deepfuzz.analyses import function_call_analyser
from deepfuzz.analyses import metadata
from deepfuzz.analyses import optimal_targets
from deepfuzz.analyses import runtime_coverage_analysis
from deepfuzz.analyses import sinks_analyser
from deepfuzz.analyses import annotated_cfg
from deepfuzz.analyses import source_code_line_analyser
from deepfuzz.analyses import far_reach_low_coverage_analyser
from deepfuzz.analyses import public_candidate_analyser

# All optional analyses.
# Ordering here is important as top analysis will be shown first in the report
all_analyses: list[type[analysis.AnalysisInterface]] = [
    optimal_targets.OptimalTargets,
    engine_input.EngineInput,
    runtime_coverage_analysis.RuntimeCoverageAnalysis,
    driver_synthesizer.DriverSynthesizer,
    bug_digestor.BugDigestor,
    filepath_analyser.FilePathAnalysis,
    function_call_analyser.ThirdPartyAPICoverageAnalyser,
    metadata.MetadataAnalysis,
    sinks_analyser.SinkCoverageAnalyser,
    annotated_cfg.FuzzAnnotatedCFG,
    source_code_line_analyser.SourceCodeLineAnalyser,
    far_reach_low_coverage_analyser.FarReachLowCoverageAnalyser,
    public_candidate_analyser.PublicCandidateAnalyser,
]

# This is the list of analyses that are meant to run
# directly from CLI without the need to generate HTML reports
standalone_analyses: list[type[analysis.AnalysisInterface]] = [
    source_code_line_analyser.SourceCodeLineAnalyser,
    far_reach_low_coverage_analyser.FarReachLowCoverageAnalyser,
    public_candidate_analyser.PublicCandidateAnalyser,
]
