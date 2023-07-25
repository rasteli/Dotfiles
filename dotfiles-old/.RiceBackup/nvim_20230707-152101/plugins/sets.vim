" Basic sets
set nocompatible            " - Disable compatibility with vi which can cause unexpected issues.
set noswapfile              " - Disable swap file.
set nobackup                " - Do not save backup files.
set splitbelow splitright   " - Sets new split to bottom and right of the window respectively.
set clipboard+=unnamedplus  " - Access to system clipboard.
set shell=/bin/bash         " - Sets shell to bash.

" Decoration sets
set nowrap               " - Do not wrap lines.
set number               " - Add numbers to each line on the left-hand side.
set relativenumber       " - Add numbers relative to the current line number.
set termguicolors        " - Enable true colors.
set showcmd              " - Show partial commands you type in the last line of the screen.
set noshowmode           " - Do not show the mode you are on the last line.
set laststatus=2         " - Enable statusline.
set fillchars+=vert:\    " - Remove pipe symbols from splits divider.

" Gui sets
set guifont=mononoki\ Nerd\ Font:h14  " - Set font used in neovide.

" Mouse and cursor sets
set mouse=a             " - Enable mouse functionality in all modes.
set cursorline          " - Highlight the cursor line.
set scrolloff=18        " - Do not let cursor scroll below or above N number of lines when scrolling.

" Tab sets
set expandtab       " - Use space characters instead of tabs.
set tabstop=2       " - Set tab width to 2 columns.
set shiftwidth=2    " - Set shift width to 2 spaces.

" Search sets
set showmatch                    " - Show matching words during search.
set incsearch                    " - While searching through a file, incrementally highlight matching characters as you type.
set smartcase                    " - Smart casing search.
set nohlsearch                   " - Do not highlight words after search.
set history=1000                 " - Set the commands to save in history.
set wildmenu                     " - Enable auto completion menu after pressing TAB.
set wildmode=longest,list,full   " - Make wildmenu behave like similar to Bash completion.

" Other settings
syntax enable               " - Turn syntax highlighting on.
"filetype off                " - Disable file type detection.
filetype plugin indent on   " - Enable indentation and plugins for the filetype.
