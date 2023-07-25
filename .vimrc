""" "Sourcering" configuration files.
runtime **/sets.vim
runtime **/plugincalls.vim
runtime **/pluginconfigs.vim
runtime **/keymaps.vim

autocmd BufWritePre * :%s/\s\+$//e              " - Remove trailing whitespaces on save.
"autocmd VimEnter * call lightline#update()      " - Update lightline when launching vim.
autocmd BufNewFile,BufRead *.gd set ft=gdscript " - Fix gdscript not being detected as a file type.
autocmd BufEnter * call ncm2#enable_for_buffer()

colorscheme onedark
"highlight CursorLine guibg=#373949
"highlight CursorLine guibg=#222d35
