import os
import random
from pathlib import Path

import cocotb
from cocotb import start_soon
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, NextTimeStep, ReadOnly, RisingEdge, Timer
from cocotb_tools.runner import get_runner



def test_simple_dff_runner():
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent.parent

    sources = [proj_path / "sources/simple_counter.sv"]

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="simple_counter",
        always=True,
    )

    runner.test(hdl_toplevel="simple_counter", test_module="test_simple_counter")
