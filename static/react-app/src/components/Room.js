import React, { useState } from 'react';

function Room({roomId,title,price,images}) {

  return (
    <a  className="row m-1" href={'http://ec2-15-164-226-5.ap-northeast-2.compute.amazonaws.com/room/detail/'+roomId } >
        <div className="col-lg-6 col-sm-12">
            <img className="rounded img-fluid" src={images[0].image} />
        </div>
        <div className="col-lg-6 col-sm-12">
            <p className="text-dark">$ {price} <b>Price/months</b></p>
            <p className="text-secondary">{title} </p>
        </div>
    </a>
  );
}

export default Room