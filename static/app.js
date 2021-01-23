// Function To Populate Dropdown
function populateDropDown () {
    // select where the dropdown is in the HTML
    let selector = d3.select('#selDataset');
    let url = "/data"
    // read the data then append all sample IDs
    d3.json(url).then((data) => {
        // let names = data.name;
        data.players.forEach((item) => {
            itemValue = item.name
            selector.append('option').text(itemValue).property('value', itemValue);
        });
    })
};

populateDropDown();