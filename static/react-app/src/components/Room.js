import React, { useState } from 'react';

function Room() {
  // Declare a new state variable, which we'll call "count"
  const [count, setCount] = useState(0);

  return (
    <a  className="row m-1" href='http://localhost:8000/room/detail/57' >
        <div className="col-6">
            <img className="rounded img-fluid" src="http://localhost:8000/media/images/photo-1540518614846-7eded433c457_D9peckk.jpg" />
        </div>
        <div className="col-6">
            <p className="text-dark">$400 <b>Price/months</b></p>
            <p className="text-secondary">Private furnished room and bathroom </p>
        </div>
    </a>
  );
}

export default Room