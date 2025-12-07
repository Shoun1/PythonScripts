function airBagsburstout(car,event){
    if (event == "Accident"){
        const airbag = new Airbag();
        airbag.burst();
        airbag.shrink();
        console.log("Passenger rescued");
    }
}