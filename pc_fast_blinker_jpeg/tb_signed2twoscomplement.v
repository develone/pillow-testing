module tb_signed2twoscomplement;

reg [9:0] res_o;
wire [8:0] z;

initial begin
    $from_myhdl(
        res_o
    );
    $to_myhdl(
        z
    );
end

signed2twoscomplement dut(
    res_o,
    z
);

endmodule
