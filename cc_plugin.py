from ccompiler.utils import NVCCCompiler

def load_ipython_extension(ip):
    cc_plugin = NVCCCompiler(ip)
    ip.register_magics(cc_plugin)