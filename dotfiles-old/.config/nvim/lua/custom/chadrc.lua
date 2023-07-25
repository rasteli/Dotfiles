local M = {}

M.plugins = "custom.plugins"
M.mappings = require "custom.mappings"

M.ui = {
  theme = "catppuccin",
  -- theme_toggle = { "gruvbox", "catppuccin" },
  transparency = true,

  statusline = {
    theme = "minimal", -- default/vscode/vscode_colored/minimal
    -- default/round/block/arrow separators work only for default statusline theme
    -- round and block will work for minimal theme only
    separator_style = "block",
  },

  nvdash = {
    load_on_startup = true,

    header = {
     "  ▄███████▄                  ▄██████▄      ▄██████▄      ▄██████▄  ",
     "▄█████████▀▀               ▄█▀████▀███▄  ▄██████████▄  ▄██████████▄",
     "███████▀      ▄▄  ▄▄  ▄▄   █▄▄███▄▄████  ███ ████ ███  ███ ████ ███",
     "███████▄      ▀▀  ▀▀  ▀▀   ████████████  ████████████  ████████████",
     "▀█████████▄▄               ██▀██▀▀██▀██  ██▀██▀▀██▀██  ██▀██▀▀██▀██",
     "  ▀███████▀                ▀   ▀  ▀   ▀  ▀   ▀  ▀   ▀  ▀   ▀  ▀   ▀",
    },
  },
}

return M
