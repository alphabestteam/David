const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2
};

const jellyfishDays = [
    [
        {color: 'pink'},
        {color: 'pink'},
        {color: 'blue'},
        {color: 'green'},
        {color: 'white'},
        {color: 'white'},
    ],
    [
        {color: 'pink'},
        {color: 'pink'},
        {color: 'blue'},
        {color: 'green'},
        {color: 'green'},
        {color: 'green'},
    ],
    [
        {color: 'pink'},
        {color: 'pink'},
        {color: 'pink'},
        {color: 'pink'},
        {color: 'blue'},
        {color: 'green'},
    ]
];

// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
    let score = 0
    console.log(`SpongeBob caught a ${jellyfish.color} jellyfish!`)
    score += identifyJellyfishAndAddPoints(jellyfish, addPoints)
    return score
}

// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish, addPoints) {
    const jellyfishSpecies = identifySpecies(jellyfish)
    console.log(`Patric identified a ${jellyfishSpecies} jellyfish!`)

    return addPoints(jellyfishSpecies)
}

// Score keeping callback function
function addPoints(species) {
    return (species in speciesPoints ? speciesPoints[species] : 1)

}

// Helper functions
function identifySpecies(jellyfish) {
    switch (jellyfish.color) {
        case "pink":
            return "pink spotted";
        case "blue":
            return "blue stinger";
        case "green":
            return "green itches";
        default:
            return "common";
    }


}

//The Adventure Starts Here! 
function startAdventure(jellyfishDays) {
    for (const jellyfishBatch of jellyfishDays) {
        let score = 0
        for (const jellyfish of jellyfishBatch) {
            score += catchJellyfish(jellyfish, identifyJellyfishAndAddPoints)
            console.log(`Score: ${score}`)
        }
        console.log("Great job, SpongeBob and Patric!")
        console.log(`Final Score: ${score}`)
    }
}

startAdventure(jellyfishDays)