local M = {}

M.general = {
  v = {
    [">"] = { ">gv", "Indent line to the right" },
    ["<"] = { "<gv", "Indent line to the left" },
  }
}

M.comment = {
  -- toggle comment in both modes
  n = {
    ["<C-_>"] = {
      function()
        require("Comment.api").toggle.linewise.current()
      end,
      "Toggle comment",
    },
  },

  v = {
    ["<C-_>"] = {
      "<ESC><cmd>lua require('Comment.api').toggle.linewise(vim.fn.visualmode())<CR>",
      "Toggle comment",
    },
  },
}

return M
