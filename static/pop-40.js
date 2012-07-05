// display songs

$(function() {
  $.getJSON('/all', function(data) {
    console.log(data)

    $.each(data, function(weekDate, rankings) {
      // build the rankings for that week
      var rows = []
      $.each(rankings, function(index, ranking) {
        rows.push('<tr><td>' + ranking.rank + '</td><td>' + ranking.song
            + '</td><td>' + ranking.artist + '</td></tr>');
      });
      $('<div/>', {
        id : weekDate,
        'class' : 'weekRank',
        html : '<h1>' + weekDate + '</h1><table>' + rows.join('') + '</table>'
      }).appendTo('#content');

    });
  }); // end getJSON

});
