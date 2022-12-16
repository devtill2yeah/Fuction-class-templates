
import bdb, pdb, sys, traceback

def excepthook(ex_type, ex_val, ex_tb):
    
    Custom exception handler to provide PDB postmortems.

    Arguments:
        ex_type Exception
            Class of ex_val.
        ex_val Exception
            Actual exception object.
        ex_tb trackback
            Call traceback object.
    
    if ex_type in (KeyboardInterrupt, bdb.BdbQuit):
        return
    elif ex_tb and not hasattr(sys, "ps1"):
        traceback.print_exception(ex_type, ex_val, ex_tb)
        pdb.post_mortem(ex_tb)
        return
    else:
        sys.__excepthook__(ex_type, ex_val, ex_tb)
        return

sys.excepthook = excepthook


