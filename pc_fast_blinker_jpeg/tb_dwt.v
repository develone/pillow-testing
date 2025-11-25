module tb_dwt;

reg [2:0] flgs;
reg upd;
reg [8:0] lft;
reg [8:0] sam;
reg [8:0] rht;
wire [9:0] lift;
wire done;
reg clock;

initial begin
    $from_myhdl(
        flgs,
        upd,
        lft,
        sam,
        rht,
        clock
    );
    $to_myhdl(
        lift,
        done
    );
end

dwt dut(
    flgs,
    upd,
    lft,
    sam,
    rht,
    lift,
    done,
    clock
);

endmodule
