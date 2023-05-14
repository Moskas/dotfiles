call plug#begin()
" Eyecandy
Plug 'ellisonleao/gruvbox.nvim'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'norcalli/nvim-colorizer.lua'
Plug 'andweeb/presence.nvim'
Plug 'lukas-reineke/indent-blankline.nvim'
Plug 'mhinz/vim-startify'

" Functionality
Plug 'ms-jpq/chadtree', {'branch': 'chad', 'do': 'python3 -m chadtree deps'}
Plug 'ms-jpq/coq_nvim', {'branch': 'coq'}
Plug 'ms-jpq/coq.artifacts', {'branch': 'artifacts'}
Plug 'akinsho/toggleterm.nvim' " Better terminal
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim', { 'tag': '0.1.0' }
Plug 'L3MON4D3/LuaSnip'
Plug 'lukas-reineke/lsp-format.nvim'
Plug 'sheerun/vim-polyglot'
Plug 'saecki/crates.nvim', { 'tag': 'v0.2.1' }

" LSP
Plug 'neovim/nvim-lspconfig'
Plug 'alexaandru/nvim-lspupdate'
Plug 'simrat39/rust-tools.nvim'

" Language support

call plug#end()

set background=dark
colorscheme gruvbox
set guifont="MesloLGS NF":8
let g:airline_theme='base16_gruvbox_dark_hard'
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#nabled = 1
let g:neovide_cursor_vfx_mode = "railgun"
lua require('extensions.setup')

nnoremap <C-o> :CHADopen<CR> 
nnoremap <C-t> :ToggleTerm<CR> 




















let g:startify_custom_header = [
 \ '                                        ▟▙            ',
 \ '                                        ▝▘            ',
 \ '██▃▅▇█▆▖  ▗▟████▙▖   ▄████▄   ██▄  ▄██  ██  ▗▟█▆▄▄▆█▙▖',
 \ '██▛▔ ▝██  ██▄▄▄▄██  ██▛▔▔▜██  ▝██  ██▘  ██  ██▛▜██▛▜██',
 \ '██    ██  ██▀▀▀▀▀▘  ██▖  ▗██   ▜█▙▟█▛   ██  ██  ██  ██',
 \ '██    ██  ▜█▙▄▄▄▟▊  ▀██▙▟██▀   ▝████▘   ██  ██  ██  ██',
 \ '▀▀    ▀▀   ▝▀▀▀▀▀     ▀▀▀▀       ▀▀     ▀▀  ▀▀  ▀▀  ▀▀',
 \ '',
 \]

