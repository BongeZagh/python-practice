function! AdjustIndent()
    let l:indent_char = "\<Tab>"
    let l:block_indent = "\<Tab>"
    let l:child_block_indent = "\<Tab>-"
    let l:grandchild_block_indent = "\<Tab>\<Tab>-"

    " Set the local buffer options for indenting
    setlocal indentexpr=GetIndent()

    " Define the GetIndent() function
    function! GetIndent()
        let l:line = getline(v:lnum)
        let l:indent_level = 0

        if l:line =~# '^'.l:block_indent.'\+'
            let l:indent_level = len(substitute(l:line, '^'.l:block_indent.'\+', '', ''))
        elseif l:line =~# '^'.l:child_block_indent.'\+'
            let l:indent_level = len(substitute(l:line, '^'.l:child_block_indent.'\+', '', ''))
        elseif l:line =~# '^'.l:grandchild_block_indent.'\+'
            let l:indent_level = len(substitute(l:line, '^'.l:grandchild_block_indent.'\+', '', ''))
        endif

        return l:indent_level * len(l:indent_char)
    endfunction

endfunction

" Call the AdjustIndent() function when opening a file
autocmd FileType markdown call AdjustIndent()

