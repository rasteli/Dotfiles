let mapleader = " "   " - Space key

" ------ Split management ------ "
nnoremap <leader>hs :split<CR>
nnoremap <leader>vs :vsplit<CR>
""" Remap navigation to just CTRL + hjkl
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l
""" Change 2 split windows from vertical to horizontal and vice-versa
nnoremap <leader>vv <C-w>t<C-w>H
nnoremap <leader>hh <C-w>t<C-w>K
""" Resizing splits
nnoremap <silent> <C-Up> :resize +3<CR>
nnoremap <silent> <C-Down> :resize -3<CR>
nnoremap <silent> <C-Left> :vertical resize +3<CR>
nnoremap <silent> <C-Right> :vertical resize -3<CR>

" ------ Tab management ------ "
nnoremap <leader>to :tabnew<CR>
nnoremap <leader>tc :tabclose<CR>
nnoremap <leader>tn :tabnext<CR>
nnoremap <leader>tp :tabprevious<CR>

" ------ Terminal ------ "
tnoremap <Esc> <C-\><C-n>
nnoremap <leader>tt :10new term://fish<CR>

" ------ Prettifying ------ "
vnoremap > >gv
vnoremap < <gv
nnoremap <A-p> :Prettier<CR>

" ------ Misc & Plugins ------ "
nmap <silent> <C-z> :set wrap!<CR>
""" Actually mapped to 'C-/'
""" for some reason, vim recognizes
""" a '/' as '_'
map <C-_> <plug>NERDCommenterToggle
nnoremap <silent> <leader>n :NERDTreeToggle<CR>
nnoremap <leader>u <Cmd>call UltiSnips#RefreshSnippets()<CR>
inoremap <silent> <expr> <CR> ncm2_ultisnips#expand_or("\<CR>", 'n')
inoremap <C-r> <C-r>=ncm2#force_trigger('ultisnips')<CR>
