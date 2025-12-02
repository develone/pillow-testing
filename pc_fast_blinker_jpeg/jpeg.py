from myhdl import *
import argparse
def signed2twoscomplement(res_o, z):
	
	@always_comb
	def unsigned_logic():
		z.next = res_o	
	return unsigned_logic
W0 = 9
t = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))  
res_o = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))
z = Signal(intbv(0)[W0:])

flgs = Signal(intbv(0)[3:])
lft = Signal(intbv(0)[W0:])
rht = Signal(intbv(0)[W0:])
sam = Signal(intbv(0)[W0:])
clock = Signal(bool(0))
upd = Signal(bool(0))
done = Signal(bool(0))
lift = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 
def dwt(flgs,upd,lft,sam,rht,lift,done,clock):
    @always(clock.posedge)
    def rtl ():
        if (upd == 1):
            done.next = 0
            if (flgs == 7):
               lift.next = sam.signed() - ((lft.signed() >> 1) + (rht.signed() >> 1))
            elif (flgs == 5):
               lift.next = sam.signed() + ((lft.signed() >> 1) + (rht.signed() >> 1))
            elif (flgs == 6):
               lift.next = sam.signed() + ((lft.signed() + rht.signed() + 2) >> 2 )
            elif (flgs == 4):
               lift.next = sam.signed() - ((lft.signed() + rht.signed() + 2) >> 2 )
        else:
            done.next = 1
    return rtl

def tb(flgs,upd,lft,sam,rht,lift,done,clock,res_o, z):
    instance_lift = dwt(flgs,upd,lft,sam,rht,lift,done,clock)
    instance_1 = signed2twoscomplement(res_o, z)
        
    @always(delay(10))
    def clkgen():
        clock.next = not clock

    @instance
    def stimulus():
        lft.next = 160
        yield clock.posedge
        sam.next = 162
        yield clock.posedge
        rht.next = 161
        yield clock.posedge
        flgs.next = 7
        yield clock.posedge
        upd.next = 1
        yield clock.posedge
        upd.next = 0
        yield clock.posedge
        sam.next = lift
        yield clock.posedge
        t.next = lift
        yield clock.posedge
        res_o.next = t[W0:]
        yield clock.posedge
        print(("lift = %4d 9 bits %s 8 bits %s ") % (lift, bin(t,W0+1),bin(t,W0+1)))        
        flgs.next = 5
        yield clock.posedge
        upd.next = 1
        yield clock.posedge
        upd.next = 0
        yield clock.posedge 
        print ('%d %s %s %s %s %s' % (now(),bin(lft,W0), bin(sam,W0), bin(rht,W0), bin(flgs,3),bin(lift,W0)))
        yield clock.posedge
 
        lft.next = 158
        yield clock.posedge
        sam.next = 159
        yield clock.posedge
        rht.next = 161
        yield clock.posedge
        flgs.next = 7
        yield clock.posedge
        upd.next = 1
        yield clock.posedge
        upd.next = 0
        yield clock.posedge
        sam.next = lift
        yield clock.posedge
        t.next = lift
        yield clock.posedge
        res_o.next = t[W0:]
        yield clock.posedge
        print(("lift = %4d 9 bits %s 8 bits %s ") % (lift, bin(t,W0+1),bin(t,W0+1)))        
        flgs.next = 5
        yield clock.posedge
        upd.next = 1
        yield clock.posedge
        upd.next = 0
        yield clock.posedge 
        print ('%d %s %s %s %s %s' % (now(),bin(lft,W0), bin(sam,W0), bin(rht,W0), bin(flgs,3),bin(lift,W0)))
        yield clock.posedge

        lft.next = 225
        yield clock.posedge
        sam.next = 224
        yield clock.posedge
        rht.next = 222
        yield clock.posedge
        flgs.next = 6
        yield clock.posedge
        upd.next = 1
        yield clock.posedge
        upd.next = 0
        yield clock.posedge
        sam.next = lift
        yield clock.posedge
        t.next = lift
        yield clock.posedge
        res_o.next = t[W0:]
        yield clock.posedge
        print(("lift = %4d 9 bits %s 8 bits %s ") % (lift, bin(t,W0+1),bin(t,W0+1)))        
        flgs.next = 4
        yield clock.posedge
        upd.next = 1
        yield clock.posedge
        upd.next = 0
        yield clock.posedge 
        print ('%d %s %s %s %s %s' % (now(),bin(lft,W0), bin(sam,W0), bin(rht,W0), bin(flgs,3),bin(lift,W0)))
        yield clock.posedge
        t.next = lift
        yield clock.posedge
        res_o.next = t[W0:]
        yield clock.posedge
        print(("lift = %4d 9 bits %s 8 bits %s ") % (lift, bin(t,W0+1),bin(t,W0+1))) 
        raise StopSimulation
    return instances()
def convert(args):
    toVerilog(dwt,flgs,upd,lft,sam,rht,lift,done,clock)
    toVerilog(signed2twoscomplement, res_o, z)
    toVHDL(dwt,flgs,upd,lft,sam,rht,lift,done,clock)
    toVHDL(signed2twoscomplement, res_o, z)
    
    #toVHDL(dwt_top,clock)
 
def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb,flgs,upd,lft,sam,rht,lift,done,clock,res_o, z)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
