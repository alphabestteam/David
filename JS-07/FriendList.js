const bobsFriends = ['patric', 'sandy', 'squidward', 'Mr. krabs', 'Gary']
console.log(bobsFriends.toString(), bobsFriends.length)
bobsFriends.push('Mrs. puff')
console.log(bobsFriends.toString(), bobsFriends.length)
bobsFriends[0] = 'Pearl' // Only the array itself is constant meaning we cant change the reference of that array but we can freely change the elements inside it
console.log(bobsFriends.toString())

