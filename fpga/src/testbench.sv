// simple test implemetation to compare sharpe ratios using if-else logic
// EDA Playground Simulation + GoBoard FPGA
// will be extended to XGBoost Machine Learning done on the FPGA

// smooth buffer of data between PC and FPGA
module FIFO_UART (
  input wr_en, input din, output full, input rd_en, rd_dout, output empty
);

assign empty = (fifo_count == 0); // DO NOT READ AT THIS STAGE
assign full = (fifo_count == depth); // DO NOT WRITE AT THIS STAGE 
// flag logic below using if-else 
// sequential logic to avoid latch behavior 
always @(posedge clk) begin

module compare_sharpe (
  // stock price is say $123 which is a 7 bit number
  // start bit vs stop bit should be accounted for later
wire[7:0] sharpe_old,
wire[7:0] sharpe_new,
output reg y

);  

// define reg and length of reg
reg [7:0] sharpe_old;
reg [7:0] sharpe_new;
// strap for UART Receiv. and Trans. 
always @(posedge clk) begin 

// comparing sharpe ratios
always @(*)begin
    if (sharpe_new == sharpe_old)
    same_res = 1;
    else
    same_res = 0;
end module


