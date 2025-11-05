// This file is public domain, it can be freely copied without restrictions.
// SPDX-License-Identifier: CC0-1.0

module simple_counter (
  input  logic clk,
  input  logic rst,
  input  logic ena,
  input  logic set,
  input  logic [7:0] din,
  output logic [7:0] counter
);

  timeunit 1ns;
  timeprecision 1ns;

endmodule