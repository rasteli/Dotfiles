local g = vim.g
local VM_maps = {}

VM_maps["Find Under"] = "<C-l>"
VM_maps["Find Subword Under"] = "<C-l>"

g.VM_maps = VM_maps

g.vimtex_view_method = "zathura"
g.vimtex_compiler_method = "latexmk"
g.vimtex_quickfix_enabled = 0

