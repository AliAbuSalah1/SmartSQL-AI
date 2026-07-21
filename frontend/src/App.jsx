import { useState } from "react";
import "./App.css";

function App() {

  const [question, setQuestion] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);


  async function askAI() {

    if (!question) return;

    setLoading(true);
    setData(null);

    try {

      const response = await fetch(
        `http://localhost:8000/ai/ask?question=${encodeURIComponent(question)}`,
        {
          method: "POST"
        }
      );


      const result = await response.json();

      setData(result);

    } catch (error) {

      setData({
        error: "Backend connection failed"
      });

    }

    setLoading(false);
  }



  return (
    <div className="container">

      <h1>SmartSQL AI</h1>

      <p>
        Ask your database using natural language
      </p>


      <div className="input-box">

        <input
          type="text"
          placeholder="Example: show me all products"
          value={question}
          onChange={(e)=>setQuestion(e.target.value)}
        />


        <button onClick={askAI}>
          Ask AI
        </button>

      </div>


      {loading && <h3>Loading...</h3>}



      {data && (

        <div className="result">


          {data.error ? (

            <h3>{data.error}</h3>

          ) : (

            <>

              <h2>Generated SQL</h2>

              <pre>
                {data.sql}
              </pre>


              <h2>Results</h2>


              <table>

                <thead>

                  <tr>

                    {data.result.length > 0 &&
                      Object.keys(data.result[0]).map((key)=>
                        <th key={key}>
                          {key}
                        </th>
                      )
                    }

                  </tr>

                </thead>


                <tbody>

                  {data.result.map((row,index)=>(

                    <tr key={index}>

                      {Object.values(row).map((value,i)=>

                        <td key={i}>
                          {value}
                        </td>

                      )}

                    </tr>

                  ))}

                </tbody>

              </table>


            </>

          )}


        </div>

      )}


    </div>
  )
}


export default App;