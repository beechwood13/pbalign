
import unittest
import os.path

import pbcommand.testkit
from pbcore.io import ConsensusAlignmentSet, openDataSet

DATA_DIR = "/mnt/secondary-siv/testdata/SA3-RS"
DATA2 = "/mnt/secondary-siv/testdata/pbalign-unittest2/data"
REF_DIR = "/mnt/secondary-siv/references"

@unittest.skipUnless(os.path.isdir(DATA_DIR), "%s missing" % DATA_DIR)
class TestPbalign(pbcommand.testkit.PbTestApp):
    DRIVER_BASE = "pbalign "
    REQUIRES_PBCORE = True
    INPUT_FILES = [
        os.path.join(DATA_DIR, "lambda", "2372215", "0007_tiny",
        "m150404_101626_42267_c100807920800000001823174110291514_s1_p0.subread.xml"),
        os.path.join(REF_DIR, "lambda", "reference.dataset.xml"),
    ]
    TASK_OPTIONS = {
        "pbalign.task_options.algorithm_options": "-holeNumbers 1-1000,30000-30500,60000-60600,100000-100500",
    }


#@unittest.skipUnless(os.path.isdir(DATA2))
@unittest.skip("disabled pending fix for blasr bug 27470")
class TestPbalignCCS(pbcommand.testkit.PbTestApp):
    DRIVER_BASE = "python -m pbalign.ccs"
    INPUT_FILES = [
        os.path.join(DATA2, "dataset.ccsreads.xml"),
        os.path.join(REF_DIR, "lambda", "reference.dataset.xml"),
    ]

    def run_after(self, rtc, output_dir):
        ds_out = openDataSet(rtc.task.output_files[0])
        self.assertTrue(isinstance(ds_out, ConsensusAlignmentSet),
                        type(ds_out).__name__)

if __name__ == "__main__":
    unittest.main()
