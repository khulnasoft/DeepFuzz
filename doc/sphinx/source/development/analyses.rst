Fuzz Introspector analyses
--------------------------

Fuzz Introspector is architected to support plugin-style development
of analysis tooling. This makes it possible to construct tooling that
uses Fuzz Introspector's core functionality and extends it for specific
applications.

This page contains details about the current analysis plugins.

All plugins are located in `src/deepfuzz/analyses <https://github.com/khulnasoft/deepfuzz/tree/main/src/deepfuzz/analyses>`_

Optimal targets
===============
.. automodule:: deepfuzz.analyses.optimal_targets
   :members:
   :show-inheritance:

Runtime coverage analysis
=========================
.. automodule:: deepfuzz.analyses.runtime_coverage_analysis
   :members:
   :show-inheritance:

Calltree analysis
=================
.. automodule:: deepfuzz.analyses.calltree_analysis
   :members:
   :show-inheritance:

Driver synthesizer
==================
.. automodule:: deepfuzz.analyses.driver_synthesizer
   :members:
   :show-inheritance:

Filepath analyser
=================
.. automodule:: deepfuzz.analyses.filepath_analyser
   :members:
   :show-inheritance:

Engine input
============
.. automodule:: deepfuzz.analyses.engine_input
   :members:
   :show-inheritance:

Sink function analyser
======================
.. automodule:: deepfuzz.analyses.sinks_analyser
   :members:
   :show-inheritance:
