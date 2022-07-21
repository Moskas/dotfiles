require'lspconfig'.pyright.setup{}
require('rust-tools').setup({})
require('toggleterm').setup{}
require("luasnip.loaders.from_vscode").lazy_load()
require'colorizer'.setup()
require("lsp-format").setup {}
require "lspconfig".gopls.setup { on_attach = require "lsp-format".on_attach }
require('crates').setup()
