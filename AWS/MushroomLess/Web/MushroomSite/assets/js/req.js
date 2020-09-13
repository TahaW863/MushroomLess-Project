axios
  .all([
    axios.get(
      'SomeAPI'
    ),
  ])
  .then((responseArr) => {
    //this will be executed only when all requests are complete
    console.log('Date created: ', responseArr[0].data);
  });
