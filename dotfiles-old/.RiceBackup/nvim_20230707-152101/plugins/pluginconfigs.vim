""" Emmet
let g:user_emmet_mode='a'                 " - Enable all modes functions in emmet-vim.
let g:user_emmet_leader_key='<C-Space>'   " - Actually the binding is <C-Space>, (with a trailing comma).

""" NERDTree
let NERDTreeShowHidden=1                            " - Show hidden files in NERDTree.
let NERDTreeCustomOpenArgs={'file':{'where': 't'}}  " - Open file in new tab in NERDTree.

""" IndentLine
let g:indentLine_char = '|'             " - Indentation character.
let g:indentLine_enabled = 1            " - Enables/Disables IndentLine.
let g:indentLine_color_term = 103       " - Color of character when true color is disable.
let g:indentLine_color_gui = '#383D4A'  " - Color of character when true color is enabled.
let g:indentLine_conceallevel = 0

""" VimTex
let maplocalleader = ','
let g:vimtex_view_method = 'zathura'
let g:vimtex_compiler_method = 'latexmk'
let g:vimtex_quickfix_enabled = 0

""" UltiSnips
let g:UltiSnipsExpandTrigger       = '<Tab>'    " use Tab to expand snippets
let g:UltiSnipsJumpForwardTrigger  = '<Tab>'    " use Tab to move forward through tabstops
let g:UltiSnipsJumpBackwardTrigger = '<S-Tab>'  " use Shift-Tab to move backward through tabstops
let g:UltiSnipsSnippetDirectories=[$HOME.'/.config/nvim/UltiSnips']

""" MultiCursors
let g:multi_cursor_start_word_key      = '<C-n>'
let g:multi_cursor_select_all_word_key = '<S-n>'
let g:multi_cursor_start_key           = 'g<C-n>'
let g:multi_cursor_select_all_key      = 'g<A-n>'
let g:multi_cursor_next_key            = '<C-n>'
let g:multi_cursor_prev_key            = '<C-p>'
let g:multi_cursor_skip_key            = '<C-x>'
let g:multi_cursor_quit_key            = '<Esc>'

""" ncm2
set completeopt=noinsert,menuone,noselect

""" Lightline configuration
"let g:lightline = {
  "\ 'colorscheme': 'one',
  "\ 'active': {
  "\   'left': [
  "\     ['mode', 'paste'],
  "\     ['gitbranch', 'readonly', 'filename', 'modified']
  "\   ]
  "\  },
  "\  'component_function': {
  "\     'gitbranch': 'gitbranch#name'
  "\   }
  "\ }

""" COC SETTINGS
"let g:coc_node_path = '/usr/local/lib/nodejs/node-v17.3.0-linux-x64/bin/node'
"command! -nargs=0 Prettier :call CocAction('runCommand', 'prettier.formatFile')
""
"let g:coc_global_extensions = [
      ""\ 'coc-pairs',
      ""\ 'coc-prettier',
      ""\ 'coc-tsserver',
      ""\ 'coc-json',
      ""\ 'coc-eslint',
      ""\ ]

""" CLOSE TAG
" filenames like *.xml, *.html, *.xhtml, ...
" These are the file extensions where this plugin is enabled.
let g:closetag_filenames = '*.html,*.xhtml,*.phtml'

" filenames like *.xml, *.xhtml, ...
" This will make the list of non-closing tags self-closing in the specified files.
let g:closetag_xhtml_filenames = '*.xhtml,*.jsx'

" filetypes like xml, html, xhtml, ...
" These are the file types where this plugin is enabled.
let g:closetag_filetypes = 'html,xhtml,phtml'

" filetypes like xml, xhtml, ...
" This will make the list of non-closing tags self-closing in the specified files.
let g:closetag_xhtml_filetypes = 'xhtml,jsx'

" integer value [0|1]
" This will make the list of non-closing tags case-sensitive (e.g. `<Link>` will be closed while `<link>` won't.)
let g:closetag_emptyTags_caseSensitive = 1

" dict
" Disables auto-close if not in a "valid" region (based on filetype)
let g:closetag_regions = {
    \ 'typescript.tsx': 'jsxRegion,tsxRegion',
    \ 'javascript.jsx': 'jsxRegion',
    \ 'typescriptreact': 'jsxRegion,tsxRegion',
    \ 'javascriptreact': 'jsxRegion',
    \ }

" Shortcut for closing tags, default is '>'
let g:closetag_shortcut = '>'

" Add > at current position without closing the current tag, default is ''
let g:closetag_close_shortcut = '<leader>>'

""" LSP CONFIG
lua << EOF
-- import lualine plugin safely
local status, lualine = pcall(require, "lualine")
if not status then
  return
end

-- get lualine nightfly theme
local lualine_onedark = require("lualine.themes.onedark")

-- new colors for theme
local new_colors = {
  blue = "#65D1FF",
  green = "#3EFFDC",
  violet = "#FF61EF",
  yellow = "#FFDA7B",
  black = "#000000",
}

-- change nightlfy theme colors
lualine_onedark.normal.a.bg = new_colors.blue
lualine_onedark.insert.a.bg = new_colors.green
lualine_onedark.visual.a.bg = new_colors.violet
lualine_onedark.command = {
  a = {
    gui = "bold",
    bg = new_colors.yellow,
    fg = new_colors.black, -- black
  },
}

-- configure lualine with modified theme
lualine.setup({
  options = {
    theme = lualine_onedark,
  },
})
--require'lspconfig'.gdscript.setup{}
require('onedark').setup {
    style = 'darker',
    transparent = true
}
EOF
