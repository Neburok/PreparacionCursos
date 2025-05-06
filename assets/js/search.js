(function (jtd, undefined) {

// Initialize lunr with the fields to be searched
function initLunr() {
  // First retrieve the index file
  return $.getJSON('/assets/js/search-data.json').then(function (loaded_data) {
    lunrIndex = lunr(function () {
      this.field('title')
      this.field('content')
      this.ref('id')

      loaded_data.docs.forEach(function (doc) {
        this.add(doc)
      }, this)
    })

    return loaded_data
  })
}

// Search for the term in the lunr index
function search(lungIndex, term) {
  return lungIndex.query(function (q) {
    const tokens = lunr.tokenizer(term)
    tokens.forEach(function (token) {
      q.term(token.toString(), {
        boost: 100
      })
      q.term(token.toString(), {
        wildcard: lunr.Query.wildcard.TRAILING
      })
    })
  })
}

$(document).ready(function () {
  const $searchInput = $('#search-input')
  const $resultRelativePath = $('#search-result-relative-path')
  const $searchResults = $('#search-results')

  let lunrIndex = null
  let loaded_data = null

  // Initialize lunrjs
  initLunr().then(function (data) {
    lunrIndex = data.index
    loaded_data = data
    $searchInput.removeAttr('disabled')
  })

  $searchInput.on('keyup', function () {
    const term = $(this).val()

    if (term === '') {
      $searchResults.empty()
      return
    }

    const results = search(lunrIndex, term)
    const $ul = $('<ul>')

    results.forEach(function (result) {
      const doc = loaded_data.docs[result.ref]
      const $li = $('<li>')
      const $link = $('<a>')
        .attr('href', doc.url)
        .text(doc.title)

      $li.append($link)
      if (doc.description) {
        $li.append($('<p>').text(doc.description))
      }
      $ul.append($li)
    })

    $searchResults.empty().append($ul)
  })
})