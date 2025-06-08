import pickle

def load_movies_from_file(file_path, pickle_path=None):
    """Load movies from a tab-delimited text file, processing every 11th row starting from row 10.
    Optionally save/load from pickle file.

    Args:
        file_path (str): Path to the text file containing movie data
        pickle_path (str): Optional path to pickle file for caching

    Returns:
        list: A list of dictionaries containing movie data
    """
    # Try to load from pickle first if path provided
    if pickle_path:
        try:
            with open(pickle_path, 'rb') as pickle_file:
                return pickle.load(pickle_file)
        except (FileNotFoundError, EOFError, pickle.PickleError):
            pass  # Proceed to load from text file

    movies = []

    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):  # Start counting from 1
                # Skip rows that aren't every 11th starting from 10
                if (line_number - 10) % 11 != 0:
                    continue

                # Skip empty lines or comment lines (starting with #)
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                # Split the line by tabs (as shown in your example)
                parts = line.split('\t')
                if len(parts) != 3:
                    print(
                        f"Warning: Invalid format in line {line_number}. Expected 3 tab-separated values, got {len(parts)}")
                    continue

                try:
                    movie_id = int(parts[0].strip())
                    short_name = parts[1].strip()
                    long_name = parts[2].strip()

                    movies.append({
                        'id': movie_id,
                        'short_name': short_name,
                        'long_name': long_name
                    })
                except ValueError:
                    print(f"Warning: Invalid ID format in line {line_number}. ID must be an integer.")

        # Save to pickle if path provided
        if pickle_path:
            try:
                with open(pickle_path, 'wb') as pickle_file:
                    pickle.dump(movies, pickle_file)
            except (pickle.PickleError, IOError) as e:
                print(f"Warning: Could not save pickle file: {str(e)}")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return movies

def loadTreeAsPickle(path=None):
    with open(path, 'rb') as file:
        return pickle.load(file)

def saveTreeAsPickle(mytree, path=None):
    with open(path, 'wb') as file:
        pickle.dump(mytree, file)