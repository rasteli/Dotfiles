local plugins = {
  {
    "mg979/vim-visual-multi",
    branch = "master",
    lazy = false
  },
  {
    "lervag/vimtex",
    event = "BufEnter *.tex"
  },
}

return plugins
