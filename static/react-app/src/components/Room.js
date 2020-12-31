import React, { useState } from 'react';

function Room({roomId,title,price,images}) {

  return (
    <a  className="row m-1" href={'http://localhost:8000/room/detail/'+roomId } >
        <div className="col-6">
            <img className="rounded img-fluid" src={"http://localhost:8000"+images[0].image} />
        </div>
        <div className="col-6">
            <p className="text-dark">$ {price} <b>Price/months</b></p>
            <p className="text-secondary">{title} </p>
        </div>
    </a>
  );
}

export default Room